package ${packagename};

/**
 * THIS CLASS IS AUTO-GENERATED - DO NOT EDIT DIRECTLY.
 * 
 * ${description}
 */

class ${classname} {

    /**
     * Defines the list of states available for ${classname}
     */
    public static enum STATE {
${statelist}
    }

    private STATE curState = ${initialstate};

${datadeclarations}

    
    ///////////////////////////////////////////////////
    // Input Value Setters
    ///////////////////////////////////////////////////
${setters}

    ///////////////////////////////////////////////////
    // Output Value Getters
    ///////////////////////////////////////////////////
${getters}

    public STATE getCurState() {
        return curState;
    }

    /**
     * Main Update Function. Steps the state machine forward
     * through one iteration.
     */
    public void update(){

        // update curState based on inputs
        // Perform state-transition actions 
        switch(curState) {
${nextstatecases}
            default:
                reset();
                break;
        }

        // assign outputs based on curState
        switch(curState) {
${stateoutputcases}
            default:
                break; //no action taken
        }

    }

    /**
     * Reset the state machine back to initial state
     */
    public void reset(){
        curState = ${initialstate}; // reset current state
    }
}