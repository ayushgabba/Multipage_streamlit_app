# Step 1: Use an official Python image as the base image
FROM python:3.8-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt .

# Step 4: Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire app into the container
COPY . .

# Step 6: Expose the port that Streamlit will run on
EXPOSE 8501

# Step 7: Set the entry point to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
