How to install python and deep learning libraries
=================================================

1. Check if your computer has an NVIDIA graphics card
-----------------------------------------------------

+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Platform**   | **Steps**                                                                                                                                                         |
+================+===================================================================================================================================================================+
| **Windows**    | 1. Open *Device Manager* (**Right-click** the *Start* button; click *Device Manager*).                                                                            |
|                | 2. Find and expand the *Display adapters* category.                                                                                                               |
|                | 3. If the list contains any device starting with *NVIDIA*, your computer is equipped with an NVIDIA GPU.                                                          |
|                | 4. Visit `Download The Official Nvidia Drivers <https://www.nvidia.com/drivers/>`_  to download and install (or update to) the latest driver for your NVIDIA GPU. |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Linux**      | 1. Open *Terminal*.                                                                                                                                               |
|                | 2. Type ``lspci | grep -i nvidia`` and press **Enter**.                                                                                                           |
|                | 3. If the command produces any text output, your computer is equipped with an NVIDIA GPU.                                                                         |
|                | 4. Visit `Download The Official Nvidia Drivers  <https://www.nvidia.com/drivers/>`_  to download and install (or update to) the latest driver for your NVIDIA GPU.|
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **macOS**      | The required NVIDIA GPU is not supported on macOS.                                                                                                                | 
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2. Check the maximum supported CUDA version of your NVIDIA GPU
--------------------------------------------------------------

If your computer is running macOS or is not equipped with an NVIDIA graphics card, please skip this step.

+----------------+---------------------------------------------------------------------------------------+
| **Platform**   | **Steps**                                                                             |
+================+=======================================================================================+
| **Windows**    | 1. Open *Command Prompt*  (Press **Win** + **R**; type ``cmd``; press **Enter**).     |
|                | 2. Type ``nvidia-smi`` and press **Enter**.                                           |
|                | 3. Look for *CUDA Version* in the output.                                             |
|                | 4. Note this version number for later.                                                |
+----------------+---------------------------------------------------------------------------------------+
| **Linux**      | 1. Open *Terminal*.                                                                   |
|                | 2. Type ``nvidia-smi`` and press **Enter**.                                           |
|                | 3. Look for *CUDA Version* in the output.                                             |
|                | 4. Note this version number for later.                                                |
+----------------+---------------------------------------------------------------------------------------+

.. note::
   Older NVIDIA GPUs may not support the ``nvidia-smi`` command or may not display *CUDA version*. 
   If this happens, try updating your graphics card drivers first and check again. 
   Otherwise, your graphics card does not support CUDA.

3. Download and install Miniconda
---------------------------------

If your computer has already installed Anaconda or Miniconda, please skip this step.

+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **Platform**   | **Installation Steps**                                                                                                                |
+================+=======================================================================================================================================+
| **Windows**    | 1. Go to `Miniconda Archive <https://repo.anaconda.com/miniconda/>`_.                                                                 |
|                | 2. Download and install the Miniconda3 latest Windows installer (ending with **x86_64.exe**).                                         |
|                | 3. Run the installer.                                                                                                                 | 
|                | 4. (Recommended) Change the default installation driver (C:).                                                                         |
|                | 5. Complete the installation.                                                                                                         |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **Linux**      | 1. Go to `Miniconda Archive <https://repo.anaconda.com/miniconda/>`_.                                                                 |
|                | 2. Download the Miniconda3 latest Linux installer (ending with **x86_64.sh** for *Intel/AMD CPUs* or **aarch64.sh** for *ARM CPUs*).  |
|                | 3. Open *Terminal* in the download folder.                                                                                            |
|                | 4. Type ``./Miniconda3-latest-Linux-x86_64.sh`` (Replace **Miniconda3-latest-Linux-x86_64.sh** with your downloaded file name).       |
|                | 5. Type ``yes`` and press **Enter** for any prompt that requires the user to type ``yes`` or ``no``.                                  |
|                | 6. Close and reopen the terminal for changes to take effect.                                                                          |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **macOS**      | 1. Go to `Miniconda Archive <https://repo.anaconda.com/miniconda/>`_.                                                                 |
|                | 2. Download the Miniconda3 latest macOS installer (ending with **arm64.pkg**).                                                        |
|                | 3. Run the installer and follow the prompts.                                                                                          |
|                | 4. Close and reopen the terminal for changes to take effect.                                                                          |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------+

4. Launch CONDA environment (for daily use)
-------------------------------------------

+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Platform**   | **Steps to Launch**                                                                                                                                    |
+================+========================================================================================================================================================+
| **Windows**    | 1. Open *Start menu*.                                                                                                                                  |
|                | 2. Find and run *Anaconda Prompt*.                                                                                                                     |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Linux**      | 1. Open *Terminal*.                                                                                                                                    |
|                | 2. If you follow Step 3, there will be ``(base)`` at the beginning of the line, indicating that the conda environment has been automatically activated.|
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **macOS**      | 1. Open *Terminal*.                                                                                                                                    |
|                | 2. If you follow Step 3, there will be ``(base)`` at the beginning of the line, indicating that the conda environment has been automatically activated.|
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

5. Create a Python 3.12 virtual environment
-------------------------------------------

Type ``conda create --name lightlin python=3.12`` in the CONDA environment and press **Enter**.
Here, ``lightlin`` is the name of the virtual environment, and you can also change it to another name.
Please wait for the execution to complete before proceeding to the next step.

6. Activate the virtual environment (for daily use)
---------------------------------------------------

Type ``conda activate lightlin`` in the CONDA environment and press **Enter**.
When the beginning of a new line changes to ``(lightlin)``, it indicates a successful virtual environment switch.
Here, ``lightlin`` needs to be replaced with the virtual environment name you taken.


7. Install PyTorch and popular point-cloud-based deep learning libraries
------------------------------------------------------------------------

Please select the corresponding command based on the result from Step 2 and run it in the activated virtual environment (such as ``lightlin``).

1. Install `PyTorch <https://pytorch.org/get-started/locally/>`_

+-------------------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **CUDA Version**        | **PyTorch Version** | **Command**                                                                                                                                            |
+=========================+=====================+========================================================================================================================================================+
| **>= 12.6**             | **cu126**           | ``pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu126``                                  |
+-------------------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **>= 11.8 and < 12.6**  | **cu118**           | ``pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu118``                                  |
+-------------------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| < 11.8                  |                     | Try updating your NVIDIA drivers and repeat step 2 to check the supported CUDA version. Otherwise, use **CPU** version.                                |
+-------------------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Unsupported**         | **cpu**             | ``pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cpu``                                    |
+-------------------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
    The macOS, non-NVIDIA GPUs, and older NVIDIA GPUs are all considered **unsupported** CUDA platforms.

2. Install `SpConv: Spatially Sparse Convolution Library <https://github.com/traveller59/spconv>`_

+---------------------+---------------------------------------------------------------+
| **PyTorch Version** | **Command**                                                   |
+=====================+===============================================================+
| **cu126**           | ``pip install spconv-cu126``                                  |
+---------------------+---------------------------------------------------------------+
| **cu118**           | ``pip install spconv-cu118``                                  |
+---------------------+---------------------------------------------------------------+
| **cpu**             | ``pip install spconv``                                        |
+---------------------+---------------------------------------------------------------+

3. Install `PyG (Pytorch Geometric) <https://pytorch-geometric.readthedocs.io/en/latest/index.html>`_

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **PyTorch Version** | **Command**                                                                                                                           |
+=====================+=======================================================================================================================================+
| **cu126**           | .. code-block:: bash                                                                                                                  |
|                     |                                                                                                                                       |
|                     |     pip install torch_geometric                                                                                                       |
|                     |     pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.1+cu126.html |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **cu118**           | .. code-block:: bash                                                                                                                  |
|                     |                                                                                                                                       |
|                     |     pip install torch_geometric                                                                                                       |
|                     |     pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.1+cu118.html |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **cpu**             | .. code-block:: bash                                                                                                                  |
|                     |                                                                                                                                       |
|                     |     pip install torch_geometric                                                                                                       |
|                     |     pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.1+cpu.html   |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------+

4. Install `NVIDIA Kaolin Library <https://developer.nvidia.com/kaolin>`_

+---------------------+-----------------------------------------------------------------------------------------------------------+
| **PyTorch Version** | **Command**                                                                                               |
+=====================+===========================================================================================================+
| **cu126**           | ``pip install kaolin==0.18.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.7.1_cu126.html`` |
+---------------------+-----------------------------------------------------------------------------------------------------------+
| **cu118**           | ``pip install kaolin==0.18.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.7.1_cu118.html`` |
+---------------------+-----------------------------------------------------------------------------------------------------------+
| **cpu**             | ``pip install kaolin==0.18.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.7.1_cpu.html``   |
+---------------------+-----------------------------------------------------------------------------------------------------------+



8. Verify Installation
----------------------

To ensure everything works properly later, please check your installation with the following steps:

1. Run Steps 4 and 6 to activate the target virtual environment.
2. Type ``pip list`` and carefully check that the suffixes of pytorch, spconv, and kaolin are consistent with each other and compatible with your *CUDA Version*.
3. Type ``python``.
4. In the output, verify that the Python version is ``3.12.X`` (you can ignore the X).
5. Type the following commands one by one and press **Enter** after each:

.. code-block:: python3

    import torch
    import spconv
    import kaolin

If no errors are reported, everything has been installed successfully! 

Finally, you can type ``exit()`` and press **Enter** to exit Python.


9. Postscript (for daily use)
-----------------------------

In the virtual environment,
you need to master how to change directories:

.. code-block:: bash

    cd "/path/to/your/project"  # For Linux/macOS

    REM For Windows
    cd /d "D:\path\to\your\project"

and execute Python files by

.. code-block:: bash

    python your_script.py

or using command-line arguments like

.. code-block:: bash

    python your_script.py -h

We also recommend that you master the basic usage methods of `conda <https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html>`_ and `pip <https://pip.pypa.io/en/stable/user_guide/>`_.