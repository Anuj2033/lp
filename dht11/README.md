# DHT Humidity Sensing on Raspberry Pi

This project is a uses the basic DHT11 python library (main method) and AdaFruit libraries (alternative method) for sensing temperature using DHT11 sensor and a Raspberry Pi.

---

> [!IMPORTANT]
> Check the [requirements](https://git.kska.io/notkshitij/DHT11/src/branch/main/REQUIREMENTS.md) first.

## Main method

> [!NOTE]
> Main method uses the `DHT11` python library for reading the sensor data.
> This is a pure Python library for reading DHT11 sensor on Raspberry Pi.

1. Install prerequisites:
```shell
sudo apt update &&\
sudo apt install -y git
```

2. Clone the project:
```shell
git clone https://git.kska.io/notkshitij/DHT11.git
```

> Alternatively, you can also [download the zip file](https://git.kska.io/notkshitij/DHT11/archive/main.zip)

3. Change the current working directory to the folder in which the project was cloned:
```shell
cd ./DHT11
```

4. Run the `setup.sh` script:
```shell
source setup.sh
```

> [!IMPORTANT]
> After running the code, and completing the execution, run `deactivate` in the terminal to exit the virtual environment.

---

## Alternative method

> [!NOTE]
> This is the alternative method, using **AdaFruit library**. This method has been tested on Raspberry Pi 3B. For easier setup, checkout [## Main method](https://git.kska.io/notkshitij/DHT11#main-method)

1. Install prerequisite packages:
```shell
sudo apt update &&\
sudo apt install git -y

```

2. Clone the project:
```shell
git clone https://git.kska.io/notkshitij/DHT11.git
```

> Alternatively, you can also [download the zip file](https://git.kska.io/notkshitij/DHT11/archive/main.zip)

3. Change the current working directory to the folder in which the project was cloned:
```shell
cd ./DHT11
```

4. Run the `ada-setup.sh` script:
```shell
source ada-setup.sh
```

> [!IMPORTANT]
> After running the code, and completing the execution, run `deactivate` in the terminal to exit the virtual environment.

---

### License

This project is licensed under the terms of the MIT license. Read the license [here](https://git.kska.io/notkshitij/DHT11/src/branch/main/LICENSE.txt).

---
