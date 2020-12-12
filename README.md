# CI/CD workflow

0.  deploy changes to git
1.  have repo deployed to VM
    - automagic using jenkins? YES, DONE
    - would jenkins need to use ansible?    DONE
2.  create/restart stack
    - creation is manual    DONE
        - the API doesn't work for non-swarm clusters
        - it works if you're not dumb
    - restarting could maybe be automated
        - use ansible?
        - or have a shell program to do it?
        - use the portainer API



looking into how to determine where a change took place in a repo

