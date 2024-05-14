# CBC and CTR Encryption in Python

This repository provides examples of how to implement CBC (Cipher Block Chaining) and CTR (Counter) encryption modes using Python.
Both mod based on block cipher that implemented in BlockCipher.py.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [CBC Mode](#cbc-mode)
  - [CTR Mode](#ctr-mode)
- [References](#references)

## Introduction

Encryption is a crucial aspect of securing data. This repository provides examples of two encryption modes:

- **CBC (Cipher Block Chaining)**: A block cipher mode that provides confidentiality by XORing each plaintext block with the previous ciphertext block before encrypting.
- **CTR (Counter)**: A block cipher mode that turns a block cipher into a stream cipher. It generates the next keystream block by encrypting successive values of a counter.

## Requirements

- Python 3.x

## Installation

First, ensure you have Python 3.x installed.
