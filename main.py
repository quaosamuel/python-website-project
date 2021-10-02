from website import create_app 
## We can do this because create app fucntion isin __init__.py which is in thr website folder ##

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)  ## Run the webserver only when the above option is satisfied ###
    


