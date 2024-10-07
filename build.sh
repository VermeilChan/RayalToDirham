#!/bin/bash

start_time=$(date +%s)

sudo apt update -y && sudo apt upgrade -y

sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev libtinfo-dev libbz2-dev libdb5.3-dev libgdbm-dev liblzma-dev tk-dev uuid-dev libreadline-dev libsqlite3-dev lld

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

buildozer android release

end_time=$(date +%s)

duration=$((end_time - start_time))

hours=$((duration / 3600))
minutes=$(((duration % 3600) / 60))
seconds=$((duration % 60))

echo "All packages have been installed successfully."
printf "Time taken: %02d hours %02d minutes %02d seconds\n" $hours $minutes $seconds
