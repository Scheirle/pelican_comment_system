#!/bin/bash

DIR_OF_THIS_FILE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ "${TRAVIS}" = "true" ]; then
	if [ "${DO_RELEASE}" != true ]; then
		exit 0
	fi
fi

cd ${DIR_OF_THIS_FILE}
pelican --debug
