# Optimizing Doctor Availability and Appointment Allocation in Hospitals through Digital Technology and Al Integration.

This Proof of Concept (POC) project aims to demonstrate how advanced digital technology and AI integration can streamline the appointment scheduling process in hospitals. By automating the identification of doctor availability and optimizing appointment slot allocation, we aim to enhance the overall patient experience and reduce waiting times.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [AI Integration](#ai-integration)
- [Contributors](#contributors)

## Introduction

In healthcare, efficient appointment scheduling is crucial to ensure patients receive timely care while maximizing the utilization of doctor resources. This project proposes a digital solution that leverages advanced technologies to automate the process of identifying doctor availability and allocate appointment slots accordingly. The primary goal is to reduce patient wait times and improve the overall efficiency of the appointment scheduling process in hospitals.

## Features

### User Dashboard

- **Disease Selection**: Users can select specific diseases (e.g., Fever, Skin, Eye) to find relevant doctors.

- **Doctor Availability**: A list of doctors specializing in the selected disease is displayed, marked in green (available) or red (unavailable) based on their current status.

- **Slot Description**: Users can view detailed slot information for each doctor, including availability and description of available slots.

- **Sorting Options**: Doctors can be sorted based on appointment time or fees, allowing patients to choose the most convenient option.

- **Booking and Registration**: When a patient selects a doctor and appointment time, a login/register popup appears for user authentication.

- **Time and Fee Adjustments**: Booking time intervals are customizable (e.g., 5 or 10 minutes), with fees adjusted accordingly.

### Doctor's Attendance

- **Manual Attendance**: Doctors have the option to manually mark their attendance using a separate dashboard.

- **Face Detection**: Alternatively, a face detection system at the entrance can automate entry and exit tracking, ensuring real-time doctor availability updates.

## Technology Stack

### AWS

- **Amazon Rekognition**: Used for face detection and recognition.

- **EC2 Instance**: Provides scalable and secure hosting.

- **S3 Bucket**: Used for data storage and retrieval.

### Generative AI

- AI algorithms are used to predict doctor availability, helping optimize appointment slots.

### Web

- **HTML, CSS (Tailwind CSS), JavaScript**: Frontend development for the user interface.

- **Django, SQL**: Backend development for managing user data, appointments, and doctor attendance.



## Usage

- Visit the website and use the user dashboard to find doctors based on disease, availability, and fees.

- Doctors can log in to mark their attendance manually or use the face detection system for automatic attendance tracking.

## AI Integration

- AI plays a crucial role in predicting doctor availability. By analyzing historical data and real-time inputs, the system can allocate appointment slots efficiently, considering factors like doctor availability and patient preferences.

- The AI model is continuously refined based on feedback and data analysis, ensuring improved scheduling accuracy over time.

## Contributors

Contributions to this project are.
- [Aarsh Saxena](https://github.com/aarshsaxena) : 21bec001
- [Kulkul Singh](https://github.com/Techkulkul) : 22bcs047
- [Pranav Kumar Kanth](https://github.com/pranavkanth) : 22bcs063
- [Tanisha Pargal](https://github.com/TanishaPargal) : 21bcs094

Mentor : [Snahal Kumar](https://github.com/snahal04) : 20bec081

Please open an issue or create a pull request to discuss and contribute.
___
---
