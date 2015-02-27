# python-databack-broker
A broker for implementing consistency and pseudo-concurrency between MongoDB and OrientDB

        - "translate" Chronos Mongo instance into OrientDB graph, with a limited mapping of properties:
        - test with MockDatastore
        - Test consistency and pseudo-concurrency (strict concurrency is not needed yet because we are going to translate low write-intensive data first)
        - Considering to use it as set of small modules to be called by a REST Node.Js layer
        
Reference diagram:


Copyright Pramantha Ltd, 2015




