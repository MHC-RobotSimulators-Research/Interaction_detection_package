execute_process(COMMAND "/home/imero/Interaction_detection_package/python_catkin/build/interaction/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/imero/Interaction_detection_package/python_catkin/build/interaction/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
