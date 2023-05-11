pipeline {
    agent any
    stages {
        stage('Push artifacts to GitHub') {
   steps {
      dir('RepoC') {
          git branch: 'pipelineC', credentialsId: 'Githubtoken', url: 'https://github.com/banupriya20/Pipeline.git'
           bat 'git add output.csv warnings.log doxygen_parser.py'
            bat 'git commit -m "Add generated artifacts"'
            bat 'git push pipelineC'
         }
      }

    }
}
}
