# Sandbox Django Forms

This repository has few examples of django's forms.

## Setup your own Sandbox Django Forms V-ENV

To experiment with this code follow the next steps:

```bash
git clone
cd SandboxFormsDjango
```

To setup the server you could use Python's Virtual Environment:

```bash
python3 -m venv v_env
```

Then enable it, on Windows:

```cmd
v_env\Scripts\activate.bat
```

Or linux and Mac OS:

```bash
source v_env/bin/activate
```

And then you install the dependencies and the start the server:

```bash
pip install -R requirements.txt
```

## Setup your own Sandbox Django Forms Docker

To use with docker you only need:

```bash
docker-compose build
docker-compose up
```
