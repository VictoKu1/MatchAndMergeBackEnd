#!/bin/bash



# Function to start the app and remember the PID of the process.
start() {
    echo "Starting app....."
    export FLASK_APP=app.py
    python3 app.py &
    echo "App started with PID: $(lsof -t -i:5001)"
    echo "App started." 
}


# Function to stop the app by killing the process with the PID saved in pid.txt.
stop() {
    echo "Stopping app....."
    kill $(lsof -t -i:5001)
    rm -rf __pycache__/ *.log pid.txt
    echo "App stopped."
}

# Fuction to check if the app is running.
status() {
    echo "Checking status....."
    # Check if the app is running by checking $(lsof -t -i:5001) is empty or not.
    if [ -n "$(lsof -t -i:5001)" ]; then
        echo "App is running with PID: $(lsof -t -i:5001)"
    else
        echo "App is not running."
    fi
}


# Function to display the help menu.
help() {
    echo "Usage: ./control.bash [start|stop|status|help]"
    echo "start: Start the app."
    echo "stop: Stop the app."
    echo "status: Check if the app is running."
    echo "help: Display this help menu."
}




# Main function to run the script.
main() {
    case $1 in
        start)
            start
            ;;
        stop)
            stop
            ;;
        status)
            status
            ;;
        help)
            help
            ;;
        *)
            help
            ;;
    esac
}


main $1