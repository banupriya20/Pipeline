pipeline {
    agent any

    stages {
      //  stage('Extend PipelineB') {
        //    steps {
          //      build 'PipelineB'
           // }
       // }
        stage('Generate Doxygen with Warnings File') {
          steps {
             dir('RepoA') {
               bat 'doxygen -g Doxyfile'
             bat "sed -i \"s|^INPUT *=.*|INPUT                  = C:/ProgramData/Jenkins/.jenkins/workspace/RepoA/src|g\" Doxyfile"
               bat 'powershell -Command "(Get-Content Doxyfile) -replace \'GENERATE_WARNING *= NO\', \'GENERATE_WARNING = YES\' | Set-Content Doxyfile"'
             bat 'powershell -Command "(Get-Content Doxyfile) -replace \'WARN_LOGFILE *=.*\', \'WARN_LOGFILE = warnings.log\' | Set-Content Doxyfile"'
            bat 'powershell -Command "(Get-Content Doxyfile) -replace \'RECURSIVE *= NO\', \'RECURSIVE = YES\' | Set-Content Doxyfile"'
            bat 'powershell -Command "(Get-Content Doxyfile) -replace \'GENERATE_HTML *= YES\', \'GENERATE_HTML = YES\' | Set-Content Doxyfile"'
                }
               dir('RepoA') {
               bat 'doxygen Doxyfile > output.log 2> warnings.log'
              bat 'copy warnings.log ..\\RepoC\\warnings.log'
            }
           }
        }
      //  stage('Clone RepoC') {
        //    steps {
          //     withCredentials([usernamePassword(credentialsId: 'Githubtoken', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
            //       bat 'git clone https://github.com/banupriya20/RepoC.git'
              //  }
          // }
       // }
               stage('Run Python with Doxygen Warnings') {
          steps {
         dir('RepoC') {
                  bat "python -u doxygen_parser.py warnings.log" 
                }
           }
        }
        stage('Push artifacts to GitHub') {
   steps {
      dir('RepoC') {
          git branch: 'pipelineC', credentialsId: 'Githubtoken', url: 'https://github.com/banupriya20/Pipeline.git'
           bat 'git add .'
            bat 'git commit -m "Add generated artifacts"'
            bat 'git push pipelineB'
         }
      }
   }
    }
}
