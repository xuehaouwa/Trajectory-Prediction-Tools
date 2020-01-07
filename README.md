# Trajectory-Prediction-Tools
![topic](https://img.shields.io/badge/topic-trajectory--prediction-brightgreen.svg?logo=github) [![HitCount](http://hits.dwyl.io/xuehaouwa/Trajectory-Prediction-Tools.svg)](http://hits.dwyl.io/xuehaouwa/Trajectory-Prediction-Tools)
[![Build Status](https://travis-ci.com/xuehaouwa/Trajectory-Prediction-Tools.svg?token=aEwVHjsxxGpNpXCgchg1&branch=master)](https://travis-ci.com/xuehaouwa/Trajectory-Prediction-Tools) ![Version](https://img.shields.io/badge/version-0.0.3-ff69b4.svg)

This `pytp` package is a tool package for the [Trajectory Prediction](https://github.com/xuehaouwa/Awesome-Trajectory-Prediction) task. It contains tools for data augmentation, normalization, preprocessing, evaluation and so on.

Maintainer - [Hao Xue](https://www.linkedin.com/in/hao-xue-491128141/)

## Installation

`pip install pytp`

## Usage

- Evaluation (calculate ADE and FDE)

  ```python
  from pytp.utils.evaluate import get_ade, get_fde
  
  ade = get_ade(predicted, ground_truth)
  fde = get_fde(predicted, ground_truth)
  ```

- Augmentation

  ```python
  from pytp.utils.augment import Augmentation
  
  aug = Augmentation()
  ```

  

## Requirements

- Python >= 3.6


## Citation

If you find this package useful, please consider citing:

```Latex
@inproceedings{xue2019pedestrian,
  title={Pedestrian Trajectory Prediction Using a Social Pyramid},
  author={Xue, Hao and Huynh, Du Q and Reynolds, Mark},
  booktitle={Pacific Rim International Conference on Artificial Intelligence},
  pages={439--453},
  year={2019},
  organization={Springer}
}
@inproceedings{xue2019location,
  title={Location-Velocity Attention for Pedestrian Trajectory Prediction},
  author={Xue, Hao and Huynh, Du and Reynolds, Mark},
  booktitle={2019 IEEE Winter Conference on Applications of Computer Vision (WACV)},
  pages={2038--2047},
  year={2019},
  organization={IEEE}
}
```



## To Do

- [ ] Documentation 
- [ ] Unit Test coverage
- [ ] Documentation website 
- [ ] Add tools for visualization
- [ ] Add model zoos to include some trajectory prediction methods


