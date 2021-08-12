# Parallel Python
> A simple demonstration of writing parallel code in python using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) package. This solution utilizes a pool object to distribute a workload across processes (an example of data parallelism).

# Usage
Running the program without any parameters will utilize the number of processes available. A specific number of processes can be specified using the --cpus argument followed by a numeric value. 

## Example
```
$ python3 parallel.py --cpus 1
Using 1 CPU(s)
Parallel execution completed in 49.47831177711487 seconds.

$ python3 parallel.py --cpus 2
Using 2 CPU(s)
Parallel execution completed in 32.50220012664795 seconds.

$ python3 parallel.py --cpus 3
Using 3 CPU(s)
Parallel execution completed in 30.893962144851685 seconds.

$ python3 parallel.py --cpus 4
Using 4 CPU(s)
Parallel execution completed in 28.359114170074463 seconds.

```

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://www.camchambers.com" target="_blank">Cam Chambers</a>.
