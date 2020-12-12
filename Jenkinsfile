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

        // deploy code to lv-426.lab, when the branch is 'dev_test'
        stage('deploy dev') {
            when { 
                expression { env.BRANCH_NAME == 'dev_test' } 
            }
            steps {
                // deploy configs to DEV
                echo 'deploy docker config files (DEV)'
                sh 'ansible-playbook ${ANSIBLE_REPO}/deploy_docker_dev.yaml'
            }
        }

        // deploy code to sevastopol.vm, when the branch is 'master'
        stage('deploy prd') {
            when { branch 'master' }
            steps {
                // deploy configs to PRD
                echo 'deploy docker config files (PRD)'
                sh 'ansible-playbook ${ANSIBLE_REPO}/deploy_docker_prd.yaml'
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

