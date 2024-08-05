import time, os

def create_dir(dir):
    try:
        os.makedirs(dir, exist_ok=False)
        print(f"Directory '{dir}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir}': {e}")

def create_folders():
    create_dir("input")
    create_dir("output")

def create_config():
    config_content = """
# This is the default config file. Edit this to your liking.
    # NOTE: settings are case sensitive, any mistakes in spelling will cause errors.
    # Refer to the github for more details. [https://github.com/smoutof/]


# Transcription settings
    # For more models and compute types, check the faster-whisper documentation. [https://github.com/SYSTRAN/faster-whisper]

language = "en"                 # language of videos [en/fi/se/etc...]
model = "small"                 # select a model [tiny/small/medium/large]
compute_type = "float32"        # select a compute type [int8/float16/float32] (if the default doesn't work, try the other ones)
device = "cpu"                  # select hardware to use [cpu/cuda]
                                    # To use an nvidia gpu, refer to the guide on the github. [https://github.com/smoutof/]



# sending emails (not recommended)
    # you must setup a sender gmail account

GMAIL_SENDING = False           # use email sending via gmail account and app [True/False]

EMAIL_ADDRESS = ""              # address of your gmail sender account [place in quotes]
EMAIL_PASSWORD = ""             # sender account's gmail app password
TO_EMAIL = ""                   # your personal email account
"""

    with open("config.py", "w") as file:
        file.write(config_content)
    print("A config.py file has been created with the default configuration.")

if __name__ == "__main__":
    input("You are about to create the config.py file with default settings. Edit the file to your liking. [enter to continue...]")
    create_config()
    create_folders()
    print("config.py created.")
    input("[enter to close]")