# Simple GPT-3 API for One-shot Procurement Classification
This project is a simple prototype aimed to give a demonstration of how fine-tuning Large Language Models like GPT-3 is a simple and very effective way of creating a recommendation system.

## API
* The API can be accessed here: [http://139.59.133.64/](http://139.59.133.64/)

## Documentation and Testing
Please refer to [http://139.59.133.64/docs](http://139.59.133.64/docs)

## About
Large language models are very powerful tools for natural language processing, and this of course includes classification tasks. In the current case of extracting attributes from a free input query, we can see that the model performs significantly well on a high level classification with just a few basic examples given directly with the prompt.

**Fine-tuning GPT-3** (or other open source language models like GPT-2) with a more suitable training set (i.e. from real use-cases) including input queries and their corresponding categories would be a simple and highly effective solution for creating a **state-of-the-art recommendation system**.

## Run Locally with Docker
You will need to setup an account at [https://openai.com/api/](https://openai.com/api/) and get your API KEY.
If you are new to Docker, click [here](https://docs.docker.com/get-started/) to install and get started.

1. Pull docker image from hub `docker pull plasticfruits/gpt3-classifier`
2. Run container `docker run -e OPENAI_API_KEY={your API KEY} --name mycontainer -p 80:80 plasticfruits/gpt3-classifier`
3. Open the URL where the app is being served [http://0.0.0.0:80]
4. Exit with `ctrl + c`

## Notes
- See `prompt.txt` for reference on the prompt text that I used.
- This is not intended as a working solution but as a demonstration of its possibilities.
