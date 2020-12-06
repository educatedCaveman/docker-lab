pipeline {
    agent any 

    environment {
        SLACK_WEBHOOK_URL = credentials('slack_webhook_url_dev_sec_ops')
    }

    stages {
        // notify
        stage('notify_start') {
            steps {
                sh 'python3 /var/lib/jenkins/slack.py ${SLACK_WEBHOOK_URL} start'
            }
        }

        // deploy code to VM
        stage('deploy') {
            steps {
                echo 'this is a new test' 
                // // use this to pass the branch/env to any helper scripts
                echo 'testing the branch name'
                echo env.BRANCH_NAME
                // sh 'python3 /var/lib/jenkins/slack.py ${SLACK_WEBHOOK_URL} start'
            }
        }
        // restart docker container
        stage('restart') {
            steps {
                // need to determine which containers to restart.
                // this depends on the changes in the repo
                echo 'this is where we restart the docker containers.  possibly a script?'
            }
        }

    }
    // notify on complete
    post {
        success {
            sh 'python3 /var/lib/jenkins/slack.py ${SLACK_WEBHOOK_URL} end'
        }
        failure {
            sh 'python3 /var/lib/jenkins/slack.py ${SLACK_WEBHOOK_URL} error'
        }
    }
}

