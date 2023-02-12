from git import Repo


PATH_OF_GIT_REPO = r'C:\Ubuntu FIles\helloworld\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.add("hellofile.txt")
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')  


f = open("hellofile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

git_push()

print("hello world")