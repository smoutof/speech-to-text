# speech-to-text
 Quick program used for speech to text using [faster-whisper](https://github.com/SYSTRAN/faster-whisper). I won't be updating this, but if you want to try it follow the guide below.

# Guide

> Note: I have only tested this program on Windows 10. I am unsure about support for other operating systems. I've also only tested this on Python 3.12

Start by downloading [Python](https://www.python.org/downloads/)

You will also need to install ffmpeg, [follow this guide](https://phoenixnap.com/kb/ffmpeg-windows).

Then clone the repository or download the zip.

    git clone https://github.com/smoutof/speech-to-text

Once everything is installed, it is recommended to create a Python environment. Open the speech-to-text folder in a terminal like PowerShell and create the environment.

    python -m venv env
Now activate the environment by running the PowerShell script in the terminal:

    .\env\Scripts\Activate.ps1
    

<details>
<summary>Can't run PowerShell scripts? (expand)</summary>
<br>

 1. Open PowerShell as administrator
 2. type `Set-ExecutionPolicy Unrestricted`
 3. Press **A**
 4. You can now close the admin window and run the script again.

</details>

Once in the environment, install the required Python packages.

    pip install -r requirements.txt

Next run the setup to generate the config file and the input/output folders.

    python setup.py
  

> run this in the root of the speech-to-text folder

Once done, feel free to edit the generated config.py to your liking.

To use the program place your video files into the input folder and run, make sure the environment is activated:

    python main.py
> run this in the root of the speech-to-text folder

Using the default config it should run fine. But if you encounter any errors try tweaking the config.

# Using GPUs

> NVIDIA required

To use an **NVIDIA** GPU the following drivers need to be installed:
 - [cuBLAS for CUDA 12](https://developer.nvidia.com/cublas)
 - [cuDNN 8 for CUDA 12](https://developer.nvidia.com/cudnn)

For a more comprehensive guide follow [this part](https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file#gpu) of the faster-whisper guide.

# Sending emails

 1. Setup a new gmail account or use an unimportant existing one.
 2. [Setup an app password](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)
 3. Enter the gmail address, app password and your personal email into the config.py file
 4. Done!

