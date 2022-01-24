import Modules

class QueryProcessor:
    query = ""
    newQuery =""

    topK = 0

    vectorDimensions = Inverted_Index.getInvertedIndexSize()
    NUMBER_OF_DOCUMENTS = FilesHelper.geNumberOfDocuments()


    ''' * queryTerms : (String, Integer) pairs:
    * String : term
    * Integer : term's appearances in query'''



    queryTerms = {}


    ##indexData : lexicon and posting lists
    indexData = Inverted_Index.getInvertedIndexData();
    ##accumulators used for the top k query
    docsAccumulators = {}

    '''
     * topKdocsVectors : (Integer, ArrayList<Double>) pair where:
    * Integer : Document Id
    * ArrayList<Double> Document's vector
    * These vectors are the vectors of the top K docs that the search engine returned after the user's
    * query.
    * These vectors are calculated if the user asks for a feedback to their query
    '''


    topKdocsVectors = {}

    ''' /*
     * docsVectors : (Integer, ArrayList<Double>) pair where:
     * Integer : Documnet Id
     * ArrayList<Double> Document's vector
     * These are vectors of the collection's documents
     * This HashMap contains the documents vectors that have been calculated so far from topKdocsVectors
     * and not all the collection's documents vectors.
     * */
    protected static HashMap<Integer, ArrayList<Double>>  /*
     * docsVectors : (Integer, ArrayList<Double>) pair where:
     * Integer : Documnet Id
     * ArrayList<Double> Document's vector
     * These are vectors of the collection's documents
     * This HashMap contains the documents vectors that have been calculated so far from topKdocsVectors
     * and not all the collection's documents vectors.
     * */
    protected static HashMap<Integer, ArrayList<Double>> '''
    docsVectors ={}

    ##Query's vector
    ##public static ArrayList<Double>
    queryVector = []

    ##The new query vector that's calculated after the feedback
    ##protected static ArrayList<Double>
    newQueryVector = []

    ##Constants that are used to the Rochio's formula to provide feedback
   ## private static final double
    A_feedBackConstant = 1.0
    B_feedBackConstant = 0.5
    C_feedBackConstant = 0.25

   ##The top K documents based on the user's query
    ##protected static ArrayList<Integer>
    topKDocs = []
    prevTopKDocs = []

    ## Lq : length of query
    Lq = 0.0

    ##contains the length of each document
    ##protected static HashMap<Integer, Double>
    docIdLdPairs = {}

    ##This variable is used to stop the running threads
    ##protected static boolean
    feedBackProvided = False

    feedBackTimes = 0

    numOfThreads = 30

    ##This queue contains the terms of the query and is used by the treads
    ##Each thread gets each term from this queue
    ##Is used to calculate the accumulators of the documents
    ##protected static LinkedBlockingQueue<String>
    queryTermsQueue = []

    ##Thread safe queue containing the id's of the top K documents
    ##Is used to calculate the top K documents vectors
    ##protected static LinkedBlockingQueue<Integer>
    queueDocIds = []

    ##Thread safe queue containing the terms of the lexicon
    ##Is used to calculate the query vector
    ##protected static LinkedBlockingQueue<String>
    queueIndexTerms = []




