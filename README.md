## MeetMind AI: Streamline Your Meetings 📝

MeetMind helps you streamline the process of managing meetings by organizing pre-meeting documents, generating agendas from key discussion points, and providing a summary of your meeting for easy reference. 
Our system aims to save time and enhance productivity, ensuring meetings are efficient and well-structured.

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Features">Features</a>
    </li>
    <li>
      <a href="#Usage-Guidelines">Usage Guidelines</a>
    </li>
    <li>
	    <a href = "#How-to-Start-Project">How to Start Project</a>
    </li>
    <li>
	    <a href = "#License">License</a>
    </li>
  </ol>
</details>

## Features
📂 **Pre-Meeting Document Uploads**: Upload relevant documents in formats like PDF, TXT, and DOCX.

📝 **Agenda Creation**: Automatically generate a structured agenda based on uploaded documents and discussion points.

📹 **Meeting Recording Analysis**: Analyze meeting recordings to identify covered and uncovered points.

📄 **Summary Generation**: Generate concise and professional summaries from meeting video.

## Usage Guidelines:
- **Step 1**: Upload pre-meeting documents and discussion points.
- **Step 2**: Our system automatically generates a well-organized agenda for the meeting.
- **Step 3**: Post-meeting, upload the meeting recording for analysis of covered and uncovered discussion points.
- **Step 4**: Receive a summary highlighting key decisions and action items, if applicable.

After the successful completion of each step you'll get a positive message in green box means you can proceed further.

## How to Start Project
Follow these steps to get started with the project:

1. **Clone the Repository:**
   ```bash
   git clone <repository_link>
   ```
2. **Install Anaconda:**
   
   Make sure you have Anaconda installed on your system. If not, you can download and install it from the official website: https://www.anaconda.com/download/
   
4. **Create a Virtual Environment:**
   
   Create a new virtual environment using Python 3.9.6:

   ```bash
   conda create --name your_env_name python=3.9.6 -y
   ```
   Replace your_env_name with the desired name for your virtual environment.

   or

   If you don't want to install anaconda then you can run the following command:
   
   ```bash
   python -m venv your_env_name
   ```
   Here you don't have the privilege to choose the python version. It will choose the default version on your computer.
   
   Activate the newly created environment:
   ```bash
   conda activate your_env_name
   ```

   or

   ```bash
   source your_env_name/bin/activate
   ```
   This command is for those who haven't created the environment using Anaconda.
5. **Install Dependencies:**
   
   Install the project dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
   This command will install all the required packages listed in the requirements.txt file.

6. **Configure Your Gemini API Key:**

   You need to create .env file in your project's root directory in which you are supposed add your own Gemini API key in the following manner:
   ```bash
   GEMINI_API_KEY = "your_gemini_api_key"
   ```

7. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
   This command will start the Streamlit app.

For the lazy individuals like me just run the following command:
   ```bash
   bash init_setup.sh
   ```
It'll perform all the steps for you except the last two steps. Isn't it good?

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Important Note ⚠️:
You must have ffmpeg installed on your computer as it's essential for the video processing portion to work properly. Please ensure ffmpeg is installed before running the application.
