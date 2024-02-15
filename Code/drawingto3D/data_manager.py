'''
Converts input mesh data to python usable data tables.

Takes in mesh data that contains vertex, UV, normal, and face data. The normal
data is discarded as it isn't used as of now and the vertex data is easily
extracted from importing the mesh with `potpourri3d`. The majority of this
code focuses on extracting and preparing the UV data and formatting the face
data as a lookup table for finding the connection between each UV and the
vertex on the 3D mesh.

Methods
-------
create_combined_data :
    Takes separate UV maps and lookup tables and combines them.
find_moved_uv_indicies :
    Return only the UVs that are within the location drawing bounds.
get_mesh_data :
    Saves out the mesh data from an obj file.
load_mesh : Loads in the mesh and creates the geodesic solver.
obj_to_txt :
    Takes in an OBJ mesh file and converts it into a text file.
txt_to_dataframe :
    Parses 3D mesh file in text format into the UV data and face lookup table.

Notes
-----
This code allows you to pull in an OBJ file for the mesh and convert it to a
text file for later use. While converting to a text file and then using that
text file seems like an unecessary step and the OBJ, file could be used
directly, converting to and saving a text file allows for the mesh data to more
quickly be used multiple times. An even faster data loading method is
implimented in `get_mesh_data` which converts to an .npz file that saves on
data space and loads quickly.

You map also note that face data is used twice. The face data is loaded by
`potpourri3d` but it also parsed in `txt_to_dataframe` to return a lookup table
for each UV on the 2D location drawing to each vertex on the 3D mesh.
'''
import numpy as np
import polars as pl
from typing import List, Tuple
import potpourri3d as pp3d


def create_combined_data(base_uv_data: Tuple[pl.DataFrame, pl.DataFrame],
                         moved_uv_data: List[Tuple[pl.DataFrame, pl.DataFrame]]
                         ) -> Tuple[pl.DataFrame, pl.DataFrame]:
    '''
    Takes separate UV maps and lookup tables and combines them.

    Takes in a base UV map and a set of maps to add to the base map. The lookup
    table of the base map has the corresponding new UVs to verticies appended
    to the end.

    Parameters
    ----------
    base_uv_data : Tuple[pl.DataFrame, pl.DataFrame]
        The main UV map to add the new UV map sections onto matched with the
        lookup table of the base UVs to the verticies on the mesh.
    moved_uv_data : List[pl.DataFrame]
        A list of UV maps to add to the base UV map matched with their lookup
        tables.

    Returns
    -------
    combined_uv_data : pl.DataFrame
        The table of the combined UV data.
    combined_lookup_data : pl.DataFrame
        The lookup table for the combined UV data.

    See Also
    --------
    find_moved_uv_indicies :
        Return only the UVs that are within the location drawing bounds.
    txt_to_dataframe :
        Parses 3D mesh file in text format into the UV data and face lookup
        table.

    Notes
    -----
    The `moved_uv_indicies` are used to find the connection between each new UV
    and the vertex on the original mesh. This breaks the 1 to 1 relation ship
    (or 2 to 1 with border UVs) of a UV to vertex. These lookup values are
    appended to the end of the base map's lookup table.
    '''
    pass


def find_moved_uv_indicies(uv_data: pl.DataFrame) -> Tuple[np.ndarray,
                                                           pl.DataFrame]:
    '''
    Return only the UVs that are within the location drawing bounds.

    In the case where the user needs to combine multiple UV maps of the same
    model, sections on the location drawing my need to be separated from the
    rest of the UV map not on the location drawing. Doing this assumes that
    the UVs have been moved somewhere past the bounds of the location drawing.

    Parameters
    ----------
    uv_data : pl.DataFrame
        UV data table in the format:

        +---+-----+-----+
        | 1 | x1  | y1  |
        +---+-----+-----+
        | 2 | x2  | y2  |
        +---+-----+-----+
        | 3 | x3  | y3  |
        +---+-----+-----+
        | 4 | ... | ... |
        +---+-----+-----+

    Returns
    -------
    moved_uv_indicies : np.ndarray
        The row numbers of the UVs in bounds used to filter the lookup table
        from the face data.
    moved_uvs : pl.DataFrame
        A table of the UVs that are in bounds of the location drawing

    See Also
    --------
    create_combined_data :
        Takes separate UV maps and lookup tables and combines them.
    txt_to_dataframe :
        Parses 3D mesh file in text format into the UV data and face lookup
        table.

    Notes
    -----
    UVs that are in bounds will have a value from 0 to 1 for both the x and y
    values. This needs to be enforced by the individual making the separated UV
    maps or else this code will not work.
    '''
    pass


def get_mesh_data(model_directory: str, obj_file: str,
                  uv_data: pl.DataFrame, lookup_table: pl.DataFrame) -> None:
    '''
    Saves out the mesh data from an obj file.

    Saves out the mesh verticies, mesh faces, the UV data, and the lookup table
    for finding the link between each UV point to a vertex on the 3D model.

    Parameters
    ----------
    model_directory : str
        The relative path to the folder that contains the UV mapped mesh files
        in obj and text format.
    obj_file : str
        The name of the obj mesh file.
    uv_data : pl.DataFrame
        Table of the UV mapping of the mesh.
    lookup_table
        Table of the connections between each UV point and mesh verticies.

    See Also
    --------
    create_combined_data :
        Takes separate UV maps and lookup tables and combines them.
    load_mesh : Loads in the mesh and creates the geodesic solver.
    txt_to_dataframe :
        Parses 3D mesh file in text format into the UV data and face lookup
        table.

    Notes
    -----
    The OBJ mesh data is used to extract the vertex table and the mesh faces.
    The text file is used by the `txt_to_dataframe` method to find the UV data
    and the lookup table from each UV point to each vertex.
    '''
    pass


def load_mesh(mesh_name: str,
              data_path: str = "../Data"
              ) -> Tuple[pp3d.MeshHeatMethodDistanceSolver,
                         pp3d.EdgeFlipGeodesicSolver,
                         np.ndarray, pl.DataFrame]:
    '''
    Loads in the mesh and creates the geodesic solver

    Loads in mesh data based on the class attributes for the mesh and
    creates a distance and path solver for the mesh
    One line summary

    Parameters
    ----------
    mesh_name : str
        The name of the mesh, i.e. Male Left Arm, Male Right Arm, Female Left
        Arm, Female Right Arm.
    data_path : str
        The relative path to the data folder containing the .npz file for the
        mesh data saved from `get_mesh_data`.

    Returns
    -------
    distance_solver : pp3d.MeshHeatMethodDistanceSolver
        Heat method solver for the mesh.
    path_solver : pp3d.MeshHeatMethodDistanceSolver
        Geodesic path solver for the mesh.
    uv_array : np.ndarry
        The x and y positions of each UV point mapped to the mesh.
    lookup_data : pl.DataFrame
        The lookup table to match UV points with mesh verticies.

    Notes
    -----
    The solvers created here are used to find the geodesic path, i.e. the
    shortest path between any two points. This is done using the Heat Method
    [#Crane]_. A solver for the path between these two points is also made that
    uses edge flips to show the path on the mesh [#2]_. Note that this path
    may not be the shortest path, just a demonstration.

    References
    ----------
    .. [#Crane] Keenan Crane, Clarisse Weischedel, and Max Wardetzky. 2013.
       Geodesics in heat: A new approach to computing distance based on heat
       flow. ACM Trans. Graph. 32, 5, Article 152 (September 2013), 11 pages
       https://doi.org/10.1145/2516971.2516977
    .. [#Sharp] Nicholas Sharp and Keenan Crane. 2020. You can find geodesic
       paths in triangle meshes by just flipping edges. ACM Trans. Graph. 39,
       6, Article 249 (December 2020), 15 pages.
       https://doi.org/10.1145/3414685.3417839


    See Also
    --------
    get_mesh_data :
        Saves out the mesh data from an obj file.
    '''
    pass


def obj_to_txt(model_directory: str, mesh_file: str) -> None:
    '''
    Takes in an OBJ mesh file and converts it into a text file.

    Parameters
    ----------
    model_directory : str
        The relative path to the folder that contains the UV mapped mesh files
        in obj format.
    mesh_file : str
        The file name of the obj mesh file.

    See Also
    --------
    txt_to_dataframe :
        Parses 3D mesh file in text format into the UV data and face lookup
        table.

    Notes
    -----
    For this text file to be useable in other code, the mesh needs to have a
    UV map that matches the location drawing template. The obj file was chosen
    because it does not change the mesh and is already in a space separated
    file format.

    The saved data has the format on each row:

    +----------------+----------+----------+----------+
    | Mesh Data Type | Column 1 | Column 2 | Column 3 |
    +----------------+----------+----------+----------+

    The vertex data looks like:

    +---+-----+-----+-----+
    | v | x1  | y1  | z1  |
    +---+-----+-----+-----+
    | v | x2  | y2  | z2  |
    +---+-----+-----+-----+
    | v | x3  | y3  | z3  |
    +---+-----+-----+-----+
    | v | ... | ... | ... |
    +---+-----+-----+-----+

    The UV data has the format:

    +----+-----+-----+
    | vt | x1  | y1  |
    +----+-----+-----+
    | vt | x2  | y2  |
    +----+-----+-----+
    | vt | x3  | y3  |
    +----+-----+-----+
    | vt | ... | ... |
    +----+-----+-----+

    The normal data has the format:

    +----+-----+-----+-----+
    | vn | x1  | y1  | z1  |
    +----+-----+-----+-----+
    | vn | x2  | y2  | z2  |
    +----+-----+-----+-----+
    | vn | x3  | y3  | z3  |
    +----+-----+-----+-----+
    | vn | ... | ... | ... |
    +----+-----+-----+-----+

    The face data has the format:

    +---+------------------+------------------+------------------+
    | f | v1,1/vt1,1/vn1,1 | v1,2/vt1,2/vn1,2 | v1,3/vt1,3/vn1,3 |
    +---+------------------+------------------+------------------+
    | f | v2,1/vt2,1/vn2,1 | v2,2/vt2,2/vn2,2 | v2,3/vt2,3/vn2,3 |
    +---+------------------+------------------+------------------+
    | f | v3,1/vt3,1/vn3,1 | v3,2/vt3,2/vn3,2 | v3,3/vt3,3/vn3,3 |
    +---+------------------+------------------+------------------+
    | f |       ...        |       ...        |       ...        |
    +---+------------------+------------------+------------------+
    '''
    pass


def txt_to_dataframe(model_directory: str,
                     file_name: str) -> Tuple[pl.DataFrame, pl.DataFrame]:
    '''
    Parses 3D mesh file in text format into the UV data and face lookup table.

    Takes in the text file created from the OBJ file of the male or female,
    right or left arm and returns the UV data and a table extracted from the
    face data. The UV data corresponds to the location template the subject
    drew on. The table from the face data serves as a lookup table between
    the UV data and their corresponding vertex in the 3D mesh.

    Parameters
    ----------
    model_directory : str
        The relative path to the folder that contains the UV mapped mesh files
        in obj format.
    file_name : str
        The name of the text mesh file.

    Returns
    -------
    uv_data : pl.DataFrame
        Table of the x and y UV values of each vertex on the location drawing.
    split_face_data : pl.DataFrame
        Lookup table of the row number of the `uv_data` table to the row
        number of the vertex table of the mesh.

    See Also
    --------
    obj_to_txt : Takes in an OBJ mesh file and converts it into a text file.

    Notes
    -----
    Takes in the text file either made from a manually cleaned obj file or from
    the `obj_to_txt` method and converts it into a polars DataFrame for use.
    This data table is then grouped by the mesh data type: verticies, uv data,
    normal data, and the face table that points to the row numbers of the
    previous three data types. This functions does not export the vertex data
    because the vertex data is pulled in any time the mesh is imported for
    analysis and the normal data is dropped because it is not needed.

    The text mesh data has the format on each row:

    +----------------+----------+----------+----------+
    | Mesh Data Type | Column 1 | Column 2 | Column 3 |
    +----------------+----------+----------+----------+

    The vertex data looks like:

    +---+-----+-----+-----+
    | v | x1  | y1  | z1  |
    +---+-----+-----+-----+
    | v | x2  | y2  | z2  |
    +---+-----+-----+-----+
    | v | x3  | y3  | z3  |
    +---+-----+-----+-----+
    | v | ... | ... | ... |
    +---+-----+-----+-----+

    The UV data has the format:

    +----+-----+-----+
    | vt | x1  | y1  |
    +----+-----+-----+
    | vt | x2  | y2  |
    +----+-----+-----+
    | vt | x3  | y3  |
    +----+-----+-----+
    | vt | ... | ... |
    +----+-----+-----+

    The normal data has the format:

    +----+-----+-----+-----+
    | vn | x1  | y1  | z1  |
    +----+-----+-----+-----+
    | vn | x2  | y2  | z2  |
    +----+-----+-----+-----+
    | vn | x3  | y3  | z3  |
    +----+-----+-----+-----+
    | vn | ... | ... | ... |
    +----+-----+-----+-----+

    The face data has the format:

    +---+------------------+------------------+------------------+
    | f | v1,1/vt1,1/vn1,1 | v1,2/vt1,2/vn1,2 | v1,3/vt1,3/vn1,3 |
    +---+------------------+------------------+------------------+
    | f | v2,1/vt2,1/vn2,1 | v2,2/vt2,2/vn2,2 | v2,3/vt2,3/vn2,3 |
    +---+------------------+------------------+------------------+
    | f | v3,1/vt3,1/vn3,1 | v3,2/vt3,2/vn3,2 | v3,3/vt3,3/vn3,3 |
    +---+------------------+------------------+------------------+
    | f |       ...        |       ...        |       ...        |
    +---+------------------+------------------+------------------+

    .. note:: There are 3 columns here because every face is a triangle.
    '''
    pass
