pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                bat 'git clone https://github.com/banupriya20/RepoA.git'
            }
        }
        
 stage('Generate Doxygen Config') {
            steps {
                 dir('RepoA') {
                    bat 'doxygen -g Doxyfile'
                 }
            }
        }

        stage('Adjust Doxygen Config') {
            steps {
                dir('RepoA') {
               bat "sed -i \"s|^INPUT *=.*|INPUT                  = C:/ProgramData/Jenkins/.jenkins/workspace/PipelineB/RepoA/src|g\" Doxyfile"
                 bat 'powershell -Command "(Get-Content Doxyfile) -replace \'RECURSIVE *= YES\', \'RECURSIVE = YES\' | Set-Content Doxyfile"'
                   bat 'powershell -Command "(Get-Content Doxyfile) -replace \'GENERATE_HTML *= YES\', \'GENERATE_HTML = YES\' | Set-Content Doxyfile"'
                    bat 'powershell -Command "(Get-Content Doxyfile) -replace \'GENERATE_LATEX *= YES\', \'GENERATE_LATEX = NO\' | Set-Content Doxyfile"'
                    //bat 'powershell -Command "(Get-Content Doxyfile) -replace \'GENERATE_WARNING *= NO\', \'GENERATE_WARNING = YES\' | Set-Content Doxyfile"'
                   // bat 'powershell -Command "(Get-Content Doxyfile) -replace \'WARN_LOGFILE *=.*\', \'WARN_LOGFILE = warnings.log\' | Set-Content Doxyfile"'
                    bat 'powershell -Command "(Get-Content Doxyfile) -replace \'RECURSIVE *= NO\', \'RECURSIVE = YES\' | Set-Content Doxyfile"'
                }
            }
        }

        stage('Run Doxygen') {
            steps {
                dir('RepoA') {
                    bat 'doxygen Doxyfile'
                }
            }
        }
        
       stage('Archive Documentation') {
   steps {
      dir('RepoA') {
         bat 'dir'
         bat 'tar -czvf doc.tar.gz html'
         archiveArtifacts 'doc.tar.gz'
      }
   }
}
    }
}
