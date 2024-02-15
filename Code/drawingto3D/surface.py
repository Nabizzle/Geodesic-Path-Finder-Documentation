'''
Takes a location drawing and converts it into a 3D surface.

Used the mesh data made for each sex and side of the body to take a location
drawing from the drawing template and create a 3D surface connected to pyvista.

Methods
-------
clean_uv_border : Removes any duplicated UV points in an array.
convert_uv_to_vertex :
    Take the UVs in the location drawing and return the verticies surface.
create_surface : Create a 3D surface from the location drawing verticies.
find_enclosed_uvs : Find all UVs contained by the location drawing.
find_uv_indicies :
    Converts the location drawing border pixels to the nearest UV values.

Notes
-----
The surface created here is connected to
`pyvista <https://docs.pyvista.org/version/stable/>`_ and can be used with any
of the functions contained in that library.
'''
import polars as pl
import numpy as np
import pyvista as pv
from typing import List


def clean_uv_border(boundary_uv_array: np.ndarray) -> List[int]:
    '''
    Removes any duplicated UV points in an array.

    Parameters
    ----------
    boundary_uv_array : np.ndarray
        A 1D array that lists all the row number of the UV array table that are
        part of the border around a location drawing.

    Returns
    -------
    clean_uv_border : List[int]
        The UV border of a location drawing with no duplicate UV points.

    See Also
    --------
    find_uv_indicies :
        Converts the location drawing border pixels to the nearest UV values.
    '''
    pass


def convert_uv_to_vertex(uv_indicies: np.ndarray, lookup_data: pl.DataFrame,
                         mesh_verticies: np.ndarray) -> np.ndarray:
    '''
    Take the UVs in the location drawing and return the verticies surface.

    Takes the row values of the UVs contained by the location drawing and
    find the corresponding verticies of the 3D mesh that make up the surface
    made by the location drawing in 3D.

    Parameters
    ----------
    uv_indicies : np.ndarray
        The row values of the UVs that make up the location drawing.
    lookup_data : pl.DataFrame
        The lookup table for finding which UVs go to which verticies.
    mesh_verticies : np.ndarray
        A Nx3 array of each vertex value.

    Returns
    -------
    location_surface : np.ndarray
        A Nx3 array of each vertex that make up the drawn location in 3D.
    '''
    pass


def create_surface(location_surface: np.ndarray) -> pv.PolyData:
    '''
    Create a 3D surface from the location drawing verticies.

    Parameters
    ----------
    location_surface : np.ndarray
        A Nx3 array of each vertex that make up the drawn location in 3D.

    Returns
    -------
    shell : pv.PolyData
        The 3D mesh from the location drawing.
    '''
    pass


def find_enclosed_uvs(uv_array: np.ndarray,
                      clean_boundary_uv_array: List[int]) -> np.ndarray:
    '''
    Find all UVs contained by the location drawing.

    Parameters
    ----------
    uv_array : np.ndarray
        Table of x, y positions of every uv point for the 3D mesh.
    clean_boundary_uv_array : List[int]
        A list of row numbers in the `uv_array` without duplicates.

    Returns
    -------
    combined_uv_indicies : np.ndarray
        Row numbers of UV values inside of and on the location drawing.

    See Also
    --------
    clean_uv_border : Removes any duplicated UV points in an array.
    find_uv_indicies :
        Converts the location drawing border pixels to the nearest UV values.

    Notes
    -----
    Uses the drawn location to bored an enclosed border around a region on the
    UV map. Then finds all the UVs inside of the border for use in extracting
    that portion of the mesh from the 3D model.
    '''
    pass


def find_uv_indicies(border_points: pl.DataFrame, uv_array: np.ndarray,
                     image_x_size: int, image_y_size: int) -> np.ndarray:
    '''
    Converts the location drawing border pixels to the nearest UV values.

    Takes the location drawing pixel locations and converts it to the index the
    closest UV values to the pixel using a KD Tree.

    Parameters
    ----------
    border_points : np.ndarray
        The x and y pixel values of a border point
    image_x_size : int
        The x dimension of the location drawing image in pixels
    image_y_size : int
        The y dimension of the location drawing image in pixels

    Returns
    -------
    border_uvs : np.ndarray
        The row numbers of the closest uv to the 2D border point list
    '''
    pass
