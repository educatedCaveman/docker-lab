pipeline {
    agent any 

    environment {
        ANSIBLE_REPO = '/var/lib/jenkins/workspace/Ansible_pipeline_master'
        SCRIPTS_REPO = '/var/lib/jenkins/workspace/Scripts_pipeline_master'
        PORTAINER_DEV_PASS = credentials('PORTAINER_DEV_PASS')
        PORTAINER_PRD_PASS = credentials('PORTAINER_PRD_PASS')
        LOCAL_REPO_DEV = '/var/lib/jenkins/workspace/Docker_Lab_dev_test'
        LOCAL_REPO_PRD = '/var/lib/jenkins/workspace/Docker_Lab_master'
    }

    stages {

        // deploy code to lv-426.lab, when the branch is 'dev_test'
        stage('deploy dev code') {
            when { 
                expression { env.BRANCH_NAME == 'dev_test' } 
            }
            steps {
                // deploy configs to DEV
                echo 'deploy docker config files (DEV)'
                sh 'ansible-playbook ${ANSIBLE_REPO}/deploy_docker_dev.yaml'
            }
        }

        // deploy to lv-426.lab whent the branch is dev_test
        stage('deploy dev stacks') {
            when { 
                expression { env.BRANCH_NAME == 'dev_test' } 
            }
            steps {
                // deploy configs to DEV
                echo 'deploy docker compose to portainer'
                sh 'python3 ${SCRIPTS_REPO}/docker/portainer_control.py --env=DEV --repo=${LOCAL_REPO_DEV}'
            }
        }

        // deploy code to sevastopol.vm, when the branch is 'master'
        stage('deploy prd code') {
            when { branch 'master' }
            steps {
                // deploy configs to PRD
                echo 'deploy docker config files (PRD)'
                sh 'ansible-playbook ${ANSIBLE_REPO}/deploy_docker_prd.yaml'
            }
        }
    }
}

