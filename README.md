# sharedLibUnderDevDockerSoloutionViaSymlinks

Add sylink to jomodul and jomodul2 in myapp/node_modules.
Now VS Code can reference and find them! Great for development!
Also your code works. 
Before deploying a docker image, replace the symlinks with the folders via

cd deplyoment
python3 replace_symlink_with_copy_of_module.py

You can undo via  

replace_modules_with_symlinks.py
