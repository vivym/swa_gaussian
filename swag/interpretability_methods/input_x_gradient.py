"""
Input x Gradient interpretability method class.
Original paper: https://arxiv.org/pdf/1605.01713.pdf
"""

import captum

from .interpretability_method import InterpretabilityMethod


class InputXGradient(InterpretabilityMethod):
    """Input x Gradient interpretability method."""

    def __init__(self, model):
        """Extends base method to include the saliency method."""
        super().__init__(model)
        self.method = captum.attr.InputXGradient(model)

    def get_saliency(self, input_batch, target_classes=None):
        """Extends base method to compute input x gradient."""
        if target_classes is None:
            target_classes = self.model(input_batch).argmax(dim=1)

        input_x_gradient = self.method.attribute(input_batch,
                                                 target=target_classes)
        input_x_gradient = input_x_gradient.detach().cpu().numpy()
        return input_x_gradient
