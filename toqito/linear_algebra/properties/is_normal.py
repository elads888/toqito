"""Determines whether or not a matrix is normal."""
import numpy as np


def is_normal(mat: np.ndarray, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
    r"""
    Determine if a matrix is normal [WIKNRM]_.

    A matrix is normal if it commutes with its adjoint

    .. math::
        \begin{equation}
            [X, X^*] = 0,
        \end{equation}

    or, equivalently if

    .. math::
        \begin{equation}
            X^* X = X X^*.
        \end{equation}

    Examples
    ==========

    Consider the following matrix

    .. math::
        A = \begin{pmatrix}
                                1 & 0 & 0 & 0 \\
                                0 & 1 & 0 & 0 \\
                                0 & 0 & 1 & 0 \\
                                0 & 0 & 0 & 1
                           \end{pmatrix}

    our function indicates that this is indeed a normal matrix.

    >>> from toqito.linear_algebra.properties.is_normal import is_normal
    >>> import numpy as np
    >>> A = np.identity(4)
    >>> is_normal(A)
    True

    Alternatively, the following example matrix :math:`B` defined as

    .. math::
        B = \begin{pmatrix}
                                1 & 2 & 3 \\
                                4 & 5 & 6 \\
                                7 & 8 & 9
                             \end{pmatrix}

    is not normal.

    >>> from toqito.linear_algebra.properties.is_normal import is_normal
    >>> import numpy as np
    >>> B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> is_normal(B)
    False

    References
    ==========
    .. [WIKNRM] Wikipedia: Normal matrix.
        https://en.wikipedia.org/wiki/Normal_matrix

    :param mat: The matrix to check.
    :param rtol: The relative tolerance parameter (default 1e-05).
    :param atol: The absolute tolerance parameter (default 1e-08).
    :return: Returns True if the matrix is normal and False otherwise.
    """
    return np.allclose(
        np.matmul(mat, mat.conj().T), np.matmul(mat.conj().T, mat), rtol=rtol, atol=atol
    )
