
# 这是一个自动生成的Python文件
def hello_world():
    print("Hello, world! Time is 'Fri Nov 10 15:09:58 2023'")


if __name__ == "__main__":
    hello_world()
    b = 1
             * \project	WonderTrader
 *
 * \author Wesley
 * \date 2020/03/30
 *
 * \brief
 */
#include "WtSimpDataMgr.h"
#include "WtExecRunner.h"
#include "../WtCore/WtHelper.h"

#include "../Share/StrUtil.hpp"
#include "../Includes/WTSDataDef.hpp"
#include "../Includes/WTSVariant.hpp"
#include "../Share/DLLHelper.hpp"
#include "../Includes/WTSSessionInfo.hpp"

#include "../WTSTools/WTSLogger.h"
#include "../WTSTools/WTSDataFactory.h"

USING_NS_WTP;


WTSDataFactory g_dataFact;

WtSimpDataMgr::WtSimpDataMgr()
	: _reader(NULL)
	, _runner(NULL)
	, _bars_cache(NULL)
	, _rt_tick_map(NULL)
{
}


WtSimpDataMgr::~WtSimpDataMgr()
{
	if (_rt_tick_map)
		_rt_tick_map->release();
}

bool WtSimpDataMgr::initStore(WTSVariant* cfg)
{
	if (cfg == NULL)
		return false;

	std::string module = cfg->getCString("module");
	if (module.empty())
		module = WtHelper::getInstDir() + DLLHelper::wrap_module("WtDataStorage");
