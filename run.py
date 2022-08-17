import uvicorn

if __name__=='__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8001, debug=True, reload=True)


# sudo docker run -p 8001:8001 -v /home/niyaz/Documents/wordify/:/home/wordify -it 6e7bfed80525 bash