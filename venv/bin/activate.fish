<<<<<<< HEAD
# This file must be used with "source bin/activate.fish" *from fish* (http://fishshell.com)
=======
# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
>>>>>>> 3c8173c20d8a60fa989096838f70d6541788a0fa
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH" 
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end
    
    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
<<<<<<< HEAD
        # set an empty local fish_function_path, so fish_prompt doesn't automatically reload
        set -l fish_function_path
        # erase the virtualenv's fish_prompt function, and restore the original
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
=======
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        . ( begin
                printf "function fish_prompt\n\t#"
                functions _old_fish_prompt
            end | psub )
        functions -e _old_fish_prompt
>>>>>>> 3c8173c20d8a60fa989096838f70d6541788a0fa
    end
    
    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
        # Self destruct!
        functions -e deactivate
    end
end

# unset irrelevant variables
deactivate nondestructive

<<<<<<< HEAD
set -gx VIRTUAL_ENV "/home/dagobailon/github_repos/policyroot/venv"
=======
set -gx VIRTUAL_ENV "/home/elainekamlley/gitrepos/policyroot/venv"
>>>>>>> 3c8173c20d8a60fa989096838f70d6541788a0fa

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

# unset PYTHONHOME if set
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.
    
<<<<<<< HEAD
    # copy the current fish_prompt function as the function _old_fish_prompt
    functions -c fish_prompt _old_fish_prompt
    
    # with the original prompt function copied, we can override with our own.
    function fish_prompt
        # Prompt override?
        if test -n ""
            printf "%s%s" "" (set_color normal)
            _old_fish_prompt
=======
    # save the current fish_prompt function as the function _old_fish_prompt
    . ( begin
            printf "function _old_fish_prompt\n\t#"
            functions fish_prompt
        end | psub )
    
    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Prompt override?
        if test -n ""
            printf "%s%s%s" "" (set_color normal) (_old_fish_prompt)
>>>>>>> 3c8173c20d8a60fa989096838f70d6541788a0fa
            return
        end
        # ...Otherwise, prepend env
        set -l _checkbase (basename "$VIRTUAL_ENV")
        if test $_checkbase = "__"
            # special case for Aspen magic directories
            # see http://www.zetadev.com/software/aspen/
<<<<<<< HEAD
            printf "%s[%s]%s " (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal) 
            _old_fish_prompt
        else
            printf "%s(%s)%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal)
            _old_fish_prompt
=======
            printf "%s[%s]%s %s" (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal) (_old_fish_prompt)
        else
            printf "%s(%s)%s%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal) (_old_fish_prompt)
>>>>>>> 3c8173c20d8a60fa989096838f70d6541788a0fa
        end
    end 
    
    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end
