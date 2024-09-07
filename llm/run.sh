#!/bin/bash

rm test_result/*
python run_food_to_recipes.py

grip -b test_result.md