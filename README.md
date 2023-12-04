# Python-RestrictedShell

*Restrict your linux / unix users in a shell with this easy to use python program.*

# **Linux Installation:**

```
git clone https://github.com/60x/Python-RestrictedShell && cd Python-RestrictedShell

sudo apt-get install python

sudo apt-get update

python shell.py
```

**Next, we need to ensure the restricted shell is applied to the user when they login. add these lines to the end of their .bashrc file:**

```
nano /home/"username"/.bashrc
```

```
trap '' 1
trap '' 2
python shell.py
```

**This uses signal handlers to stop the user from exiting the restricted shell environment,**
**using Control keys.**
