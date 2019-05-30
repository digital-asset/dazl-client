apt-get update && apt-get install -y \
    python3-pip

pip3 install /tmp/dazl*.whl

echo "\$HOME is set to $HOME"
cd /root/test && python3 integration-test.py
