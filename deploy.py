# 1. local git based
# 2. github only to show code
# 3. master=production
# 4. New dev in branches
# 5. webapp in app folder
# 6. deplyment scripts as part of repo
# 7. deploy.py script does pipeline:
# 	1. Checks if not flags any([STAGED_TO_DEPLOY, READY_TO_DEPLOY])
# 	2. Set flag on branch -> STAGED_TO_DEPLOY (.gitignore? gitpython wrapper)
# 	3. Local tests
# 	4. If passed: Deploy to test_server
# 	5. Tests on test_server
# 	6. I all_passed: Set flag on branch -> READY_TO_DEPLOY
# 	7. Script turns off

# 8. User should test manualy test_server
# 9. If tests OK, user does: git merge master ~~? OR deploy_production.py ??? GIT hooks?
# 	1. If READY_TO_DEPLOY and good branch checkedout
# 	2. Commits to master
# 	3. Deploys on production server
# 	4. Basic Tests on prduction server

# 10. User deploy -> pushes on github
import Fabric





if "__main__" == __name__:
    main()