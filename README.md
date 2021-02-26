# auction-monitor

build image 
docker build --pull --rm -f "Dockerfile" -t auctionmonitor:latest "."

run image without proxy
docker run --rm -i auctionmonitor:latest


run image with proxy
docker run --rm -e "http_proxy=????" -e "https_proxy=????" -i auctionmonitor:latest