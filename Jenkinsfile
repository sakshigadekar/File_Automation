pipeline 

{
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sakshigadekar/File_Automation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t file-manager:latest .'
            }
        }

        stage('Run Rename Test') {
            steps {
                sh 'docker run --rm file-manager rename --folder /app/file_manager/test_files || true'
            }
        }

        stage('Run Move Test') {
            steps {
                sh 'docker run --rm file-manager move --source /app/file_manager/test_files --destination /app/file_manager/sorted || true'
            }
        }

        stage('Run Cleanup Test') {
            steps {
                sh 'docker run --rm file-manager cleanup --folder /app/file_manager/logs --size 1 || true'
            }
        }
    }
}

