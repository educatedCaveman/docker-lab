# CI/CD workflow

0.  deploy changes to git
1.  have repo deployed to VM
    - automagic using jenkins?
    - would jenkins need to use ansible?
2.  create/restart stack
    - creation is manual
        - the API doesn't work for non-swarm clusters
    - restarting could maybe be automated
        - use ansible?
        - or have a shell program to do it?