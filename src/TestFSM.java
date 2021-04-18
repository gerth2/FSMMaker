package frc.robot.lib;

/**
 * THIS CLASS IS AUTO-GENERATED - DO NOT EDIT DIRECTLY.
 * 
 * Test configuration for auto-generated state machines
 */

class TestFSM {

    /**
     * Defines the list of states available for TestFSM
     */
    public static enum STATE {
        TESTSTATE1,
        TESTSTATE2,

    }

    private STATE curState = STATE.TESTSTATE1;

    private double sampleInput1;
    private boolean sampleOutput1;
    private double sampleOutput2;


    
    ///////////////////////////////////////////////////
    // Input Value Setters
    ///////////////////////////////////////////////////
    public void setsampleInput1( double val ) {
        sampleInput1 = val;
    }


    ///////////////////////////////////////////////////
    // Output Value Getters
    ///////////////////////////////////////////////////
    public double getsampleOutput2() {
        return sampleOutput2;
    }


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
            case TESTSTATE1:
                if(true){
                    sampleOutput2 = sampleInput1;
                    curState = STATE.TESTSTATE2;
                    break;
                }

            break;

            case TESTSTATE2:
                if(true){
                    sampleOutput2 = 100.0;
                    curState = STATE.TESTSTATE1;
                    break;
                }

            break;


            default:
                reset();
                break;
        }

        // assign outputs based on curState
        switch(curState) {
            case TESTSTATE1:
                sampleOutput1 = false;
                break;
            case TESTSTATE2:
                sampleOutput1 = true;
                break;

            default:
                break; //no action taken
        }

    }

    /**
     * Reset the state machine back to initial state
     */
    public void reset(){
        curState = STATE.TESTSTATE1; // reset current state
    }
}