
quick demo project for my friend to show how to:

- make a simple web server that streams data
- make a simple mobile app that receives data from the web server
## Dependencies
- python
- python-poetry
- npm
### Optional
- make
- adb (for android)
- xcode + a mac (for ios, not tested by me)

## Usage
    
### run the server
    cd server
    make

### run the mobile app
    cd mobile && npm i && npx expo start

### for development, proxy the port so that you can access localhost:8000 on your phone
    adb reverse tcp:8000 tcp:8000
