import torch
import torch.nn as nn


class GroupNorm(nn.Module):
    """
    Custom GroupNorm implementation without using nn.GroupNorm or F.group_norm.

    Divides the C channels into G groups and normalizes over [C/G, *spatial]
    independently for each group and each batch element.

    Supports any number of spatial dimensions: [B, C, L], [B, C, H, W], etc.

    y = (x - mean) / sqrt(var + eps) * weight + bias
    """

    def __init__(self, num_groups: int, num_channels: int, eps: float = 1e-5):
        super().__init__()
        assert num_channels % num_groups == 0, (
            f"num_channels ({num_channels}) must be divisible by num_groups ({num_groups})"
        )
        self.G = num_groups
        self.C = num_channels
        self.eps = eps

        # Learnable affine parameters, one per channel
        self.weight = nn.Parameter(torch.ones(num_channels))
        self.bias = nn.Parameter(torch.zeros(num_channels))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, C = x.shape[:2]
        assert C == self.C, (
            f"Expected input with {self.C} channels, but got {C} channels."
        )
        spatial = x.shape[2:]  # e.g. (L,) or (H, W)

        # Correct reshape: [B, G, C//G, *spatial]
        x = x.view(B, self.G, C // self.G, *spatial)

        # Normalize over per-group channels and spatial dims
        dims = tuple(range(2, x.ndim))
        mean = x.mean(dim=dims, keepdim=True)
        var = x.var(dim=dims, keepdim=True, unbiased=False)
        x = (x - mean) / torch.sqrt(var + self.eps)

        # Restore to [B, C, *spatial]
        x = x.view(B, C, *spatial)

        # Apply affine transform: [C] -> [1, C, 1, ...]
        affine_shape = (1, C) + (1,) * len(spatial)
        return x * self.weight.view(affine_shape) + self.bias.view(affine_shape)