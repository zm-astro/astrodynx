import jax.numpy as jnp
from jax.typing import ArrayLike
from jax import Array


def rotmat3dx(angle: ArrayLike) -> Array:
    r"""
    Returns a 3D rotation matrix for a given angle in radians.

    Args:
        angle: The angle in radians to rotate around the x-axis.
    Returns:
        A 3x3 rotation matrix that rotates vectors around the x-axis by the specified angle.
    Notes:
        The rotation matrix is defined as:
        $$
        R_x(\theta) = \begin{bmatrix}
        1 & 0 & 0 \\
        0 & \cos(\theta) & -\sin(\theta) \\
        0 & \sin(\theta) & \cos(\theta)
        \end{bmatrix}
        $$
        where $\theta$ is the angle of rotation.
    References:
        Battin, 1999, pp.85.
    Examples:
        A simple example of creating a rotation matrix for a 90-degree rotation (π/2 radians):

        >>> import jax.numpy as jnp
        >>> from astrodynx.utils import rotmat3dx
        >>> angle = jnp.pi / 2
        >>> rotmat3dx(angle)
        array([[ 1.,  0.,  0.],
               [ 0.,  0., -1.],
               [ 0.,  1.,  0.]])

    """
    c = jnp.cos(angle)
    s = jnp.sin(angle)
    return jnp.array([[1, 0, 0], [0, c, -s], [0, s, c]])
