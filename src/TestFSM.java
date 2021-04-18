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
        ALLDONE,

    }

    private STATE curState = STATE.TESTSTATE1;

    private double sampleInput1;
    private boolean internalDataTest;
    private double sampleOutput1;


    
    ///////////////////////////////////////////////////
    // Input Value Setters
    ///////////////////////////////////////////////////
    public void setsampleInput1( double val ) {
        sampleInput1 = val;
    }


    ///////////////////////////////////////////////////
    // Output Value Getters
    ///////////////////////////////////////////////////
    public double getsampleOutput1() {
        return sampleOutput1;
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
                if(sampleInput1>20.0){
                    // Take transition 3
                    sampleOutput1 = sampleInput1;
                    curState = STATE.TESTSTATE2;
                    break;
                }

            break;

            case TESTSTATE2:
                if(internalDataTest==true){
                    // Take transition 2
                    sampleOutput1 = 100.0;
                    curState = STATE.TESTSTATE1;
                    break;
                }

                if(true){
                    // Take transition 1
                    curState = STATE.ALLDONE;
                    break;
                }

            break;

            case ALLDONE:
            break;


            default:
                reset();
                break;
        }

        // assign outputs based on curState
        switch(curState) {
            case TESTSTATE1:
                internalDataTest = false;
                break;
            case TESTSTATE2:
                internalDataTest = true;
                break;
            case ALLDONE:
                internalDataTest = true;
                sampleOutput1 = -321.135;
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