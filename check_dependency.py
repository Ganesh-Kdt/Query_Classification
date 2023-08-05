import json
import logging
from datetime import date
import boto3
import pymilvus
import fitz
import re
import sentence_transformers
from flask import Flask, request

print('all dependencies installed')