import os
import io
import paramiko

def check_hosts(remote_host,ssh):
    """
    Checks if the host is already in the known hosts file and only updates the connection as needed.
    BUG: Does not work. Eventually need to resolve issue.

    Parameters
    ----------
    remote_host : TYPE
        DESCRIPTION.
    ssh : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    # Check if the known_hosts file exists and if it contains the remote host
    known_hosts_path = os.path.expanduser('~/.ssh/known_hosts')

    if not os.path.exists(known_hosts_path) or remote_host not in open(known_hosts_path).read():
        # Set the missing host key policy if the host is missing
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # return ssh

def read(filepath,host,username,password):

    # Set up SSH connection to the remote system
    ssh = paramiko.SSHClient()

    # Check host file
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote system
    ssh.connect(hostname=host, username=username, password=password)
        
    # Open an SFTP session using paramiko
    sftp = ssh.open_sftp()
    
    # Open the remote file as a file-like object
    remote_file = sftp.open(filepath, 'r')
    
    # Read the file contents into memory
    file_contents = remote_file.read()
    
    # Close the file and the SFTP session
    remote_file.close()
    sftp.close()
    
    # Close the SSH connection
    ssh.close()
    
    return file_contents

def write(obj,filepath,host,username,password):

    # Set up SSH connection to the remote system
    ssh = paramiko.SSHClient()

    # Check host file
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote system
    ssh.connect(hostname=host, username=username, password=password)
        
    # Open an SFTP session using paramiko
    sftp = ssh.open_sftp()
    
    # Store the object on the remote system
    sftp.putfo(obj, filepath)
    
    # Close the SFTP session
    sftp.close()
    
    # Close the SSH connection
    ssh.close()