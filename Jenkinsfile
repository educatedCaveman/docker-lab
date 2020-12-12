pipeline {
    agent any 

    environment {
        SLACK_WEBHOOK_URL = credentials('slack_webhook_url_dev_sec_ops')
        JENKINS_SCRIPTS = '/var/lib/jenkins/workspace/Jenkins_self_deploy'
        ANSIBLE_REPO = '/var/lib/jenkins/workspace/Ansible_pipeline_master'
    }

    stages {
        // notify
        stage('notify_start') {
            steps {
                sh 'python3 ${JENKINS_SCRIPTS}/slack.py ${SLACK_WEBHOOK_URL} start'
                echo env.BRANCH_NAME
            }
        }

        // deploy code to VM
        stage('deploy dev') {
            when { 
                expression { env.BRANCH_NAME == 'dev_test' } 
            }
            steps {
                // // use this to pass the branch/env to any helper scripts
                echo 'test running ansible'
                sh 'ansible-playbook ${ANSIBLE_REPO}/deploy_docker_dev.yaml -vvvv'
            }
        }

        // deploy code to VM
        stage('deploy prd') {
            when { branch 'master' }
            steps {
                // // use this to pass the branch/env to any helper scripts
                echo 'testing the branch name'
                echo env.BRANCH_NAME
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
            sh 'python3 ${JENKINS_SCRIPTS}/slack.py ${SLACK_WEBHOOK_URL} end'
        }
        failure {
            sh 'python3 ${JENKINS_SCRIPTS}/slack.py ${SLACK_WEBHOOK_URL} error'
        }
    }
}

