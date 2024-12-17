# Qualcomm QRB ROS Documentation

## Read online documents

QRB ROS Documents: [quic-qrb-ros.github.io](https://quic-qrb-ros.github.io)

## Build documents

Install sphinx and themes

```bash
sudo pip install sphinx sphinx-rtd-theme sphinx-design sphinx-tabs sphinx-multiversion
```

Build and generate html

```bash
make html
cp source/_templates/index.html build/html/
```

## Preview web page

```bash
cd build/html
python3 -m http.server
```

Then, in browser open `http://your_host:8000` to preview..
