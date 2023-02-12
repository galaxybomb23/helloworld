from git import Repo


PATH_OF_GIT_REPO = r'C:\Ubuntu FIles\helloworld\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script 1'

def git_push(message: str):
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.add("hellofile.txt")
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')  


f = open("hellofile.txt", "a")

for i in range(5):
    mess = f"Test commit {i} / 5"
    f.write(f"Now the file has more content! {i}\n")
    git_push(mess)

f.close()

print("hello world")